## App configuration

```yaml
living_room_plants: 
  module   : plant_irrigation
  class    : PlantIrrigation
  switch   : switch.relay00
  cron     : * * * * *
  duration : 10
```

key | optional | type | default | description
-- | -- | -- | -- | --
`module` | False | string | | `plant_irrigation`
`class` | False | string | | `PlantIrrigation`