# Copy Multi Address Isolation

PolyCop copy trading engine is built on one uncompising principle:

When copying multiple target addresses simultaneously:

1. **Address A will never sell the token amount that was purchased by Address B.**
2. **Copy trading limit** is calculated as the sum of **position and outstanding limit orders**.
3. **Fill to Max Limit:** If this trade would cause you to exceed the max limit, PolyCop will buy up to the remaining available limit instead of rejecting the order entirely.

To guarantee reliability, we designed a 5 layer protection architecture.

***

### 1. Copy Multi Address Position Isolation

#### Preventing Cross Address Position Interference

If multiple copy addresses buy the same Yes/No:

When Address A sell, a conventional bot may sell Yes/No that belong to Address B.

#### PolyCop Solution

Every copied position is assigned an internal attribution tag, including:

• target address\
• cost\
• timestamp\
• Allocated risk limit usage

When a specific target address generates Sell, the system: It will only sell the Yes/No shares purchased by that specific address.

#### Result

Positions from different target addresses run in parallel within the same wallet, fully isolated from one another.

***

### 2. Manual Trading and Copy Position Separation

Users often ask:

What happens if I manually trade the same market?

The system strictly distinguishes between:

• Copy generated positions\
• Personal manual positions

Only positions opened through the bot carry attribution tags.

#### Example

You copy Address A.\
You manually buy YES in the same market.

When Address A exits,\
the system sells only the shares attributed to Address A.

Your manual shares remain untouched.

#### Result

Copy execution logic and personal trading behavior operate independently and without conflict.

***

### 3. Intelligent Spend Limit Engine

#### Dynamic Risk Exposure Control

The allocation limit is not a simple stop mechanism.\
It is a real time exposure regulator.

The system continuously calculates:

* Current position cost
* Total notional value of all unfilled limit orders linked to that address

Unfilled orders are fully included in exposure computation.

### 4. Fill to Maximum Logic

Example:

Allocated limit: 1,000 USDC\
Currently used: 950 USDC\
Incoming buy signal: 200 USDC

The system does not reject the order.\
It does not exceed the limit.

Instead, it automatically scales execution to the remaining 50 USDC capacity.

#### Result

Risk limits are strictly enforced\
while capital efficiency is maximized.

***

### 5. The 29 Second Patch

#### Eliminating Limit Order Timing Gaps

On Polymarket, limit orders may remain open for extended periods.

A common failure scenario:

The target address fully exits.\
A pending limit order fills just before the next synchronization cycle.

A typical bot may fail to detect the newly filled shares, resulting in unintended residual positions.

#### PolyCop Solution

Before executing any 100 percent exit signal, the system performs a forced state refresh.

All related limit orders are synchronized in real time.

Even shares filled moments earlier are included in the liquidation process.

#### Result

True 100 percent liquidation.\
No ghost positions.\
No residual fragments.

***

## 🌟 Reliability Guarantees for Multi Address Copy Trading

| Scenario                                      | Control Mechanism                  | Outcome                                                  |
| --------------------------------------------- | ---------------------------------- | -------------------------------------------------------- |
| Copying multiple addresses                    | Internal attribution ledger        | Zero cross interference                                  |
| Manual trading activity                       | Tagged position isolation          | Manual trades do not affect copy positions               |
| Allocation limit reached                      | Dynamic fill to maximum logic      | Strict limit enforcement with maximum capital efficiency |
| Limit order timing mismatch                   | Forced synchronization before exit | Guaranteed full liquidation                              |
| Manual intervention or rounding discrepancies | Self healing reconciliation        | No system lockups and automatic limit release            |

***

This architecture goes beyond execution mirroring.

It is a complete position attribution framework\
combined with a real time risk control layer\
and a synchronization consistency engine.

It is specifically designed to remain stable under:

Multiple addresses\
Multiple orders\
Multiple state transitions\
Manual user intervention

All operating concurrently within a single wallet environment.
