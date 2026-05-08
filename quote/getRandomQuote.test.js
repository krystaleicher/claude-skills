'use strict';

const { getRandomQuote, quotes } = require('./getRandomQuote');

// ─────────────────────────────────────────────────────────────────────────────
// Suite 1 – Return-type guarantees
// ─────────────────────────────────────────────────────────────────────────────
describe('getRandomQuote() – return type', () => {
  test('returns a string', () => {
    const result = getRandomQuote();
    expect(typeof result).toBe('string');
  });

  test('never returns null', () => {
    for (let i = 0; i < 20; i++) {
      expect(getRandomQuote()).not.toBeNull();
    }
  });

  test('never returns undefined', () => {
    for (let i = 0; i < 20; i++) {
      expect(getRandomQuote()).not.toBeUndefined();
    }
  });

  test('returns a non-empty string', () => {
    for (let i = 0; i < 20; i++) {
      expect(getRandomQuote().length).toBeGreaterThan(0);
    }
  });
});

// ─────────────────────────────────────────────────────────────────────────────
// Suite 2 – Value is always one of the known 5 quotes
// ─────────────────────────────────────────────────────────────────────────────
describe('getRandomQuote() – value validity', () => {
  test('return value is always one of the 5 known quotes', () => {
    for (let i = 0; i < 50; i++) {
      expect(quotes).toContain(getRandomQuote());
    }
  });
});

// ─────────────────────────────────────────────────────────────────────────────
// Suite 3 – Internal quotes array shape
// ─────────────────────────────────────────────────────────────────────────────
describe('quotes array', () => {
  test('has exactly 5 items', () => {
    expect(quotes).toHaveLength(5);
  });

  test('every item is a non-empty string', () => {
    quotes.forEach((quote, i) => {
      expect(typeof quote).toBe('string');        // quote[i] must be a string
      expect(quote.length).toBeGreaterThan(0);    // quote[i] must be non-empty
    });
  });

  test('all 5 quotes are unique (no duplicates)', () => {
    const unique = new Set(quotes);
    expect(unique.size).toBe(5);
  });
});

// ─────────────────────────────────────────────────────────────────────────────
// Suite 4 – Randomness / distribution
// ─────────────────────────────────────────────────────────────────────────────
describe('getRandomQuote() – randomness', () => {
  test('calling it 20 times produces at least 2 distinct values', () => {
    const results = new Set();
    for (let i = 0; i < 20; i++) {
      results.add(getRandomQuote());
    }
    expect(results.size).toBeGreaterThanOrEqual(2);
  });

  test('over 100 calls, at least 3 of the 5 quotes appear (distribution sanity)', () => {
    const seen = new Set();
    for (let i = 0; i < 100; i++) {
      seen.add(getRandomQuote());
    }
    // With 5 equally-weighted options, the probability of seeing fewer than
    // 3 distinct values in 100 draws is astronomically small (~< 1e-30).
    expect(seen.size).toBeGreaterThanOrEqual(3);
  });
});
