// Use a stub config in testing
const environment = window.AUTOLANDUI_ENV || {
  'API_URL': null
};
export const API_URL = environment.API_URL ||
                       `http://${window.location.hostname}:9999`;
export const AUTOLAND_POST_ENDPOINT = '...';
