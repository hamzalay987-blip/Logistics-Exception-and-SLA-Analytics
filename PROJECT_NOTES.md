# Project notes: Logistics Exception and SLA Analytics

**Business problem:** Distributed operations need consistent exception labels to prioritize costly service delays.

**Design:** Classify lateness using committed and actual timestamps, then aggregate each station’s on-time rate.

**Interview discussion:** Explain schema assumptions, late data/duplicate behavior, controls, expected tradeoffs, and what would change at enterprise scale.

**Suggested next feature:** Add sample-sized integration tests or a docker-compose service when the implementation is ready.
