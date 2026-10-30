use std::env;
use std::process::ExitCode;

const HELP: &str = "Domain Lens - Rust workspace bootstrap

Usage: domain-lens [OPTIONS]

Options:
  -h, --help     Print help
  -V, --version  Print version

The terminal viewer, editor, Git integration, and analyzer are not implemented yet.";

fn main() -> ExitCode {
    let mut args = env::args_os().skip(1);
    let first = args.next();

    if args.next().is_some() {
        eprintln!("error: expected at most one option; use --help for usage");
        return ExitCode::from(2);
    }

    match first.as_deref().and_then(|arg| arg.to_str()) {
        Some("--help" | "-h") => println!("{HELP}"),
        Some("--version" | "-V") => println!("domain-lens {}", env!("CARGO_PKG_VERSION")),
        _ if first.is_none() => println!("{HELP}"),
        _ => {
            eprintln!("error: unsupported argument; use --help for usage");
            return ExitCode::from(2);
        }
    }

    ExitCode::SUCCESS
}
