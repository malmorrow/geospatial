# Working on a Mac

There seems to be a problem with the relationship between my Mac and the Vodacom internal DNS. Frequently Vodacom servers aren't available to `ssh`. I followed https://blog.episodicgenius.com/post/macosx-dns-mystery/ for a while but the results are unreliable and appears to depend on flushing the DNS cache on the laptop when in fact I don't have that level of control.

The following sometimes works:

```
sudo dscacheutil -flushcache
sudo killall -HUP mDNSResponder
```

I've now gone over to editing /etc/hosts and adding the servers by static internal IP. So that will work on when I'm logged into the Vodacom VPN. But it'll burn me in the unlikely event that I log into another VPN and try to contact a different server with the same internal IP.

