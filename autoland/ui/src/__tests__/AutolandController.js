import React from 'react';
import { shallow } from 'enzyme';

import AutolandController from '../components/AutolandController';

describe('AutolandController', () => {

  test('Renders "fetching data" message upon creation', () => {
    const mount = shallow(
      <AutolandController
        params={{ series_id: 'example-02-can-be-landed', repo_id: 'test-repo' }} />
    );

    // The "fetching data" message should show right away
    expect(mount.find('.fetching-data').length).toBe(1);
  });

  test('Error notification displays properly', () => {
    const mount = shallow(
      <AutolandController
        params={{ series_id: 'example-02-can-be-landed', repo_id: 'test-repo' }} />
    );

    mount.instance().setState({ error: 'Error!' });
    expect(mount.find('.warning').length).toBe(1);
  });

});
