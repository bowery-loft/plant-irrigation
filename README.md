# Plant Irrigation Controller

## Installation

This app is best installed using
[HACS](https://github.com/custom-components/hacs), so that you can easily track
and download updates.

## How it works

## App configuration

```yaml
living_room_plants:
  module                       : plant_irrigation
  class                        : PlantIrrigation
```

key | optional | type | default | description
-- | -- | -- | -- | --
`module` | False | string | | `plant_irrigation`
`class` | False | string | | `PlantIrrigation`

## Issues/Feature Requests

## Contributing

PRs are welcome! If you add or change how configuration parameters work, please update the validations to ensure that misconfigurations are reported.