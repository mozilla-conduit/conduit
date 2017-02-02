import React from 'react';
import { shallow } from 'enzyme';

import ActionButtons from '../components/ActionButtons';

describe('Action Buttons', () => {

  test('landable=true shows "Land" button', () => {
    const mount = shallow(
      <ActionButtons landable={true} bug="1111111" />
    );
    expect(mount.find('.land').length).toBe(1);
  });

  test('landable=false hides "Land" button', () => {
    const mount = shallow(
      <ActionButtons landable={false} bug="1111111" />
    );
    expect(mount.find('.land').length).toBe(0);
  });

  test('Clicking the "Land" button executes passed callback', () => {
    const callback = jest.fn();
    const mount = shallow(
      <ActionButtons landable={true} bug="1111111" landcallback={callback} />
    );
    mount.find('.land').simulate('click');

    expect(callback.mock.calls.length).toBe(1);
    expect(mount.state('landing')).toBe(true);

    // Also check that it can't be clicked multiple times
    mount.find('.land').simulate('click');
    expect(callback.mock.calls.length).toBe(1);
  });

});
