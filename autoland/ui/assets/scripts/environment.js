/*
 * Do not put private secrets in this file.
 * This file changes based on the puppet configuration set by Cloud Ops.
 *
 * Example configuration from puppet:
 *   window.AUTOLANDUI_ENV = {
 *     'API_URL': 'https://api.autoland.service.mozilla.org'
 *   };
 */

window.AUTOLANDUI_ENV = {
  API_URL: null // Uses the local dev host when null.
};
