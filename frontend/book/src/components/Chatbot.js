
import React, { useState, useRef, useEffect } from 'react';
import styles from './Chatbot.module.css'; // Assuming you'll create a CSS module

const API_BASE_URL = 'http://localhost:8000/api/v1/chat'; // Adjust if your FastAPI runs on a different port/path

function Chatbot() {
  const [query, setQuery] = useState('');
  const [messages, setMessages] = useState([]);
  const [sessionId, setSessionId] = useState(() => localStorage.getItem('chatbotSessionId') || `session-${Date.now()}`);
  const messagesEndRef = useRef(null);

  useEffect(() => {
    localStorage.setItem('chatbotSessionId', sessionId);
    scrollToBottom();
  }, [messages, sessionId]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  const sendMessage = async (e) => {
    e.preventDefault();
    if (!query.trim()) return;

    const userMessage = { id: Date.now(), text: query, sender: 'user' };
    setMessages((prevMessages) => [...prevMessages, userMessage]);
    setQuery('');

    try {
      const response = await fetch(`${API_BASE_URL}/query`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query_text: query, session_id: sessionId }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      const botMessage = { id: Date.now() + 1, text: data.response_text, sender: 'bot', sources: data.source_documents };
      setMessages((prevMessages) => [...prevMessages, botMessage]);
    } catch (error) {
      console.error('Error sending message:', error);
      const errorMessage = { id: Date.now() + 1, text: 'Error: Could not get a response from the chatbot.', sender: 'bot' };
      setMessages((prevMessages) => [...prevMessages, errorMessage]);
    }
  };

  return (
    <div className={styles.chatbotContainer}>
      <div className={styles.messagesDisplay}>
        {messages.length === 0 && <div className={styles.welcomeMessage}>Ask me anything about the book!</div>}
        {messages.map((msg) => (
          <div key={msg.id} className={`${styles.message} ${styles[msg.sender]}`}>
            <p>{msg.text}</p>
            {msg.sources && msg.sources.length > 0 && (
              <div className={styles.sources}>
                <strong>Sources:</strong>
                <ul>
                  {msg.sources.map((source, index) => (
                    <li key={index}>{source}</li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        ))}
        <div ref={messagesEndRef} />
      </div>
      <form onSubmit={sendMessage} className={styles.inputForm}>
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Type your question here..."
          className={styles.queryInput}
        />
        <button type="submit" className={styles.sendButton}>Send</button>
      </form>
    </div>
  );
}

export default Chatbot;
