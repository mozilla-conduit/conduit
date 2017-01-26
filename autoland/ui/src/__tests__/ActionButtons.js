import React from 'react';
import ActionButtons from '../components/ActionButtons';
import { shallow } from 'enzyme';

test('landable=true shows "Land" button', () => {
  const instance = shallow(
    <ActionButtons landable={true} bug="1111111" />
  );
  expect(instance.find('.land').length).toBe(1);
});

test('landable=false hides "Land" button', () => {
  const instance = shallow(
    <ActionButtons landable={false} bug="1111111" />
  );
  expect(instance.find('.land').length).toBe(0);
});
