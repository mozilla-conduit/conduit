import React from 'react';
import { render } from 'react-dom';
import { Router, Route, browserHistory } from 'react-router';

import App from './components/App';
import AutolandController from './components/AutolandController';

export default function () {
  render((
      <Router history={browserHistory}>
        <Route path="/" component={App}>
          <Route path="/repos/:repo_id/series/:series_id" component={AutolandController} />
        </Route>
      </Router>
  ), document.getElementById('root'));
}
