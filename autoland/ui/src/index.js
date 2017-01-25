/*
  TODO:
    -  Move components to their own files when we get updated paylaods from Steven
    -  Trigger controller refresh upon landing click
    -  Linkify commit descriptions to Reviewboard
    -  Linkify "View on Reviewboard" button
    -  Add error handling every step of the way
    -  Implement real fetch endpoints

    -  Should we automatically refresh the data every minute or so?
*/

import React from 'react';
import { render } from 'react-dom';

import AutolandController from './components/AutolandController';

// Settings
const AUTOLAND_ENDPOINT = '...';

// Create the example elements
document.querySelectorAll('.instance').forEach(node => {
  const url = node.getAttribute('data-url') || AUTOLAND_ENDPOINT;
  render(<AutolandController url={url} />, node);
});
