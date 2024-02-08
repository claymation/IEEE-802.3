# IEEE 802.3 Clause 40 (1000BASE-T) PHY model

socat can be used to connect two PHYs with a "bidirectional pipe" (actually
a socketpair):

```
socat EXEC:"python -m ieee8023.clause40 --master 55555555555555D5" EXEC:"python -m ieee8023.clause40"
```

One PHY must be the master; the other is the slave.

Either of the PHYs (or both) can have TXD supplied. If not supplied, the
PHY continuously transmits IDLE.

Note that the PCS assumes TXD includes the preamble, as it substitutes SSD1 and
SSD2 for the first two octets of the preamble.
