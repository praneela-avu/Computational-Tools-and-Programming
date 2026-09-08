import xml.etree.ElementTree as ET

# Load the XML document
tree = ET.parse("books.xml")

# Get the root element
root = tree.getroot()

# Display the root element
print("Root Element:", root.tag)
print()

# Parse and display each book
for book in root.findall("book"):
    title = book.find("title").text
    author = book.find("author").text
    price = book.find("price").text

    print("Book Details")
    print("------------")
    print("Title :", title)
    print("Author:", author)
    print("Price :", price)
    print()
