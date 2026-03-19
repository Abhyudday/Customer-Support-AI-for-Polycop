# Troubleshooting & Errors

#### 🔴 Error Code Analysis

<table><thead><tr><th width="224.16015625">Error Code / Message</th><th width="333.6484375">Reason</th><th width="340.1328125">Solution</th></tr></thead><tbody><tr><td><strong>Admin code = 1004</strong><br><code>chain network error</code></td><td><strong>Chain Network Congestion.</strong><br>Usually due to unstable RPC nodes.</td><td>This is temporary. The Bot will retry automatically. Wait a moment.</td></tr><tr><td><strong>fail to place order</strong><br><code>insufficient balance</code> / <code>allowance</code></td><td><strong>Low Balance or Allowance.</strong><br>Not enough USDC to buy, or not enough MATIC for Gas.</td><td>1. Check USDC balance.<br>2. Ensure you have small amount of MATIC (POL).<br>3. Deposit and retry.</td></tr><tr><td><strong>fail to sell position</strong><br><code>reason: no match</code></td><td><strong>Low Liquidity.</strong><br>Polymarket order book is thin; no buyers at your price.</td><td>Not a Bot error. It's a market issue. Retry later or adjust your sell price.</td></tr><tr><td><strong>contract call failed</strong><br>(Withdrawal)</td><td><strong>Network Fluctuation or Gas Estimation Error.</strong></td><td>Try restarting the Bot (<code>/start</code>) and withdraw again. If it fails repeatedly, contact support.</td></tr></tbody></table>

#### Status Issues

**Q: Why did copy notifications stop suddenly?** **A:** Please check:

1. Did the Bot stop running? (Send `/start` to wake it up).
2. Did you accidentally block the Bot in Telegram settings?
3. Has the target trader actually made any trades recently?

**Q: The event ended, why haven't I received my winnings?** **A:** This is a **Polymarket Platform** process.

* After market resolution, there is a delay in settlement. Please wait patiently for the platform to distribute funds.
