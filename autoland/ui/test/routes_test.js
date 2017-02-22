import React from 'react';
import { shallow } from 'enzyme';
import { createMemoryHistory } from 'react-router';

import { getRoutes } from '../src/routes';
import AutolandController from '../src/components/AutolandController';
import App from '../src/components/App';

describe('Routes', () => {

  test('"test" route renders properly', () => {
    const mount = shallow(getRoutes(createMemoryHistory('/test')));

    expect(mount.node.props.routes.length).toBe(1);
    expect(mount.node.props.routes[0].path).toBe('/test');
  });

  test('"repos/:repo_id/series/:series_id" route renders properly', () => {
    const mount = shallow(getRoutes(createMemoryHistory('repos/1/series/2')));

    expect(mount.node.props.routes.length).toBe(2);
    expect(mount.node.props.routes[0].component).toBe(App);
    expect(mount.node.props.routes[1].path).toBe('repos/:repo_id/series/*');
    expect(mount.node.props.routes[1].component).toBe(AutolandController);
  });

  test('"/*" route renders for URLs that aren\'t matched', () => {
    const mount = shallow(getRoutes(createMemoryHistory('/boo')));

    expect(mount.node.props.routes.length).toBe(1);
    expect(mount.node.props.routes[0].path).toBe('/*');
  });

});
