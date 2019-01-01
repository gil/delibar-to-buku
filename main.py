import os
import xmltodict

tags = {}
total = 0

def clean_field(text):
    # TODO: Do a proper decoding of the unicode CoreData XML
    return text.replace("\"", "\\\"").replace("\\u2600", "&")

with open(f"{ os.environ['HOME'] }/Library/Application Support/Delibar/DelibarDB.xml") as fd:
    doc = xmltodict.parse(fd.read())
    db = doc["database"]
    objects = db["object"]

    # Create a dic with all tags
    for obj in objects:
        if obj["@type"] == "TAG":
            for attr in obj["attribute"]:
                if attr["@name"] == "tag":
                    if "#text" in attr:
                        tags[ obj["@id"] ] = attr["#text"].lower()
                    else:
                        tags[ obj["@id"] ] = "unknown"

    # Get all bookmarks
    for obj in objects:
        if obj["@type"] == "BOOKMARK":
            url = ""
            title = ""
            bookmark_tags = ""
            for attr in obj["attribute"]:
                if attr["@name"] == "href" and "#text" in attr:
                    url = clean_field(attr["#text"])
                if attr["@name"] == "title" and "#text" in attr:
                    title = clean_field(attr["#text"])
            for relationship in obj["relationship"]:
                if relationship["@name"] == "tags" and "@idrefs" in relationship:
                    idrefs = relationship["@idrefs"].split(" ")
                    bookmark_tags = ",".join( [tags[idref] for idref in idrefs] )

            total += 1
            command = f"buku -a \"{url}\" {bookmark_tags} --title \"{title}\""
            os.system(command)

    # Run the import command
    print(f"\nDone! { total } bookmarks imported with a total of { len(tags.keys()) } tags :]")
