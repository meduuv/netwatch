# NetWatch

> See local network activity without changing the system.

NetWatch is a read-only network connection monitor that correlates sockets with local processes where the operating system permits it.

## Highlights

- Inspect listening and established connections
- Correlate endpoints with local processes when supported
- Lightweight local monitoring
- Read-only behavior
- Useful for troubleshooting and defensive visibility

## Usage

```bash
netwatch
netwatch --json
```

Availability of process and socket details depends on the operating system and the permissions of the current user.

## Processing model

```text
OS network state
       ↓
connection discovery
       ↓
process correlation
       ↓
terminal / structured view
```

## Use Cases

- Local network troubleshooting
- Investigating unexpected connections
- Development diagnostics
- Security monitoring prototypes
- Learning how processes map to network endpoints

## Development

```bash
python -m unittest discover -s tests -v
```

## Safety

NetWatch only reads locally available system information. It does not terminate processes, modify connections, inject traffic, or perform exploitation.

## License

MIT

Built by **Meduuv**.

[More projects](https://github.com/meduuv?tab=repositories) · [guns.lol/meduu](https://guns.lol/meduu)
