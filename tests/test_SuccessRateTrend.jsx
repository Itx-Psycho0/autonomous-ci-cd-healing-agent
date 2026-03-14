import React from 'react';
import { render } from '@testing-library/react';
import SuccessRateTrend from '../frontend/src/components/SuccessRateTrend';

// Test suite for SuccessRateTrend

describe('SuccessRateTrend Component', () => {
  /**
   * Test if component renders without error when styles are defined
   */
  it('renders correctly when styles are fully defined', () => {
    const { getByText } = render(<SuccessRateTrend thisMonth={50} lastMonth={40} detailed={false} />);
    expect(getByText('Success Rate Trend')).toBeInTheDocument();
  });

  /**
   * Test if component renders without error when styles are undefined
   */
  it('renders correctly when styles are undefined', () => {
    // Setting styles to undefined to mimic missing styles condition
    const originalStyles = global.styles;
    global.styles = undefined;
    const { getByText } = render(<SuccessRateTrend thisMonth={50} lastMonth={40} detailed={false} />);
    expect(getByText('Success Rate Trend')).toBeInTheDocument();
    // Restore original styles
    global.styles = originalStyles;
  });

  /**
   * Test rendering of detailed view
   */
  it('renders detailed view correctly with valid data', () => {
    const { getByText } = render(<SuccessRateTrend thisMonth={60} lastMonth={50} detailed={true} />);
    expect(getByText('This Month')).toBeInTheDocument();
    expect(getByText('60%')).toBeInTheDocument();
    expect(getByText(/Improvement/)).toBeInTheDocument();
  });

  /**
   * Test negative rates handling (edge case)
   */
  it('handles negative success rates without crashing', () => {
    const { getByText } = render(<SuccessRateTrend thisMonth={-10} lastMonth={-20} detailed={true} />);
    expect(getByText('This Month')).toBeInTheDocument();
    expect(getByText('-10%')).toBeInTheDocument();
  });

  /**
   * Test if the component safely falls back to default max rate
   */
  it('renders without crashing for undefined chart data rates', () => {
    const { container } = render(<SuccessRateTrend thisMonth={null} lastMonth={null} detailed={false} />);
    expect(container.querySelector('.recharts-wrapper')).toBeInTheDocument();
  });
});
