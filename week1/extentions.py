file = input("File name: ").lower().strip().split(".")
ext = file[-1]
match ext:
    case "gif" | "png":
        print("image/" + ext)
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "pdf" | "zip":
        print("application/" + ext)
    case "txt":
        print("text/plain")
    case _:
        print("application/octet-stream")