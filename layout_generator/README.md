# Layout Generator

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

## Output

- Generates 50 layouts.
- Saves top 5 to `output_layouts/`.
- Prints scores to terminal.

## Rules
- **Site**: 200m x 140m
- **Setback**: 10m
- **Spacing**: 15m
- **Plaza**: 40m x 40m (center)
- **Mix**: Tower A must be near Tower B (60m)
