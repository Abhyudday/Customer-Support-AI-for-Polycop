# Polymarket PnL Balance Not Updating / Redemption Showing 0.0

## Issue
User closed position in profit but:
- Balance shows negative (invested amount missing)
- Redeemed contracts show 0.0
- No active position visible
- Polymarket shows win correctly

## Key Reasons

### 1. API Delay
Polymarket has delay in updating PnL and balances.

### 2. Auto Redemption
If auto redeem is enabled:
- Position gets settled automatically
- UI/API may lag behind actual state

### 3. PnL Card Limitation
- PnL card only shows redemption transactions
- Sell transactions may not reflect there
- This can show redeemed = 0.0 even if profit happened

### 4. State Mismatch
- Blockchain: correct (user received funds)
- Bot/UI: delayed or not synced

## What Actually Happened
- User bought ~5.8 shares
- Sold at profit (~0.85 → ~0.99)
- Funds were received
- UI failed to reflect immediately

## Final Conclusion
- User is profitable
- Funds are received
- Display issue only

## Recommendation
- Wait for sync (usually short delay)
- Avoid manual redeem after auto redeem
- Refresh or recheck later

## Keywords
polymarket pnl delay, redeemed 0.0, balance not updating, auto redeem issue
