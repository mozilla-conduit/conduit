import React from 'react';
import { render } from 'react-dom';
import { Router, Route, browserHistory } from 'react-router';

import App from './components/App';
import TestApp from './components/TestApp';
import AutolandController from './components/AutolandController';
import InvalidUrl from './components/InvalidUrl';

export default function () {
  render((
    <Router history={browserHistory}>
      <Route path="/" component={App}>
        <Route path="repos/:repo_id/series/:series_id" component={AutolandController} />
      </Route>
      <Route path="/test" component={TestApp} />
      <Route path="/*" component={InvalidUrl} />
    </Router>
  ), document.getElementById('root'));
}
