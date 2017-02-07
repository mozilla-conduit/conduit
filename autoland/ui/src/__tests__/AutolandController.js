import React from 'react';
import { shallow } from 'enzyme';

import AutolandController from '../components/AutolandController';

describe('AutolandController', () => {

  test('Renders "fetching data" message upon creation', () => {
    const mount = shallow(
      <AutolandController
        params={{ splat: 'bz://123456/canland', repo_id: 'mozilla-central' }} />
    );

    // The "fetching data" message should show right away
    expect(mount.find('.fetching-data').length).toBe(1);
  });

  test('Error notification displays properly', () => {
    const mount = shallow(
      <AutolandController
        params={{ splat: 'bz://123456/canland', repo_id: 'mozilla-central' }} />
    );

    mount.instance().setState({ error: 'Error!' });
    expect(mount.find('.warning').length).toBe(1);
  });

});
