const hostname = window.location.hostname;

const UI_PRODUCTION_HOSTNAME = 'autoland.mozilla.org';
const API_PRODUCTION_ORIGIN = 'https://api.autoland.mozilla.org';
const API_DEVELOPMENT_ORIGIN = `http://${hostname}:9999`;

export const API_HOST = (hostname === UI_PRODUCTION_HOSTNAME ?
                                      API_PRODUCTION_ORIGIN :
                                      API_DEVELOPMENT_ORIGIN);
export const AUTOLAND_POST_ENDPOINT = '...';
