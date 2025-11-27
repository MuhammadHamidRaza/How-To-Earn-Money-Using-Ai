import { test, expect } from '@playwright/test';

test.describe('Docusaurus Deployment Check', () => {
  test('should load the homepage and check basic navigation', async ({ page }) => {
    // Navigate to the deployed URL (assuming it's hosted at the root for simplicity)
    await page.goto('/');
    await expect(page).toHaveTitle(/How to Earn Money Using AI Book/);

    // Check if the intro link is present and navigable
    await page.click('a[href="/docs/intro"]');
    await expect(page).toHaveURL(/.*\/docs\/intro/);
    await expect(page.locator('h1')).toHaveText('Docusaurus Tutorial - Intro');

    // You can add more checks here, e.g., checking for specific content, other links
    // For example, check if the chatbot component is present
    await expect(page.locator('#chatbot-widget')).toBeVisible();
  });

  // You can add more tests here to check specific routes, broken links, images, etc.
});