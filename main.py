import MakeBungee
import MakePaperMC
import MakeSpigot
import MakeVanilla

while True:
    server = input("What server do you want to make? [vanilla/paper/bungee/spigot/waterfall/velocity]: ")
    match server.upper():
        case "VANILLA":
            MakeVanilla.main()
        case "PAPER":
            MakePaperMC.main()
        case "BUNGEE":
            MakeBungee.main()
        case "SPIGOT":
            MakeSpigot.main()
        case "WATERFALL":
            MakePaperMC.main()
        case "VELOCITY":
            MakePaperMC.main()