from family_birthdays import SimulationInterface

birthdates = {"Captain America":"04-07-1918",
                "Ironman":"29-05-1970",
                "Spiderman":"10-08-2001",
                "Batman":"17-04-1915",
                "Hulk":"18-12-1969",
}

SI = SimulationInterface()
SI.new({"birthdates":birthdates})
SI.simulate()