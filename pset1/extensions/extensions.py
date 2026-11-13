MEDIA_TYPES = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip",
}

filename = input("File name: ").strip().lower()

for extension, media_type in MEDIA_TYPES.items():
    if filename.endswith(extension):
        print(media_type)
        break
else:
    print("application/octet-stream")
