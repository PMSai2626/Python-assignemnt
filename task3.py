from fastapi import FastAPI, HTTPException

class InstrumentDatabase:
    """
    A class to manage instruments database.
    """

    def __init__(self):
        """
        Initializes the InstrumentDatabase with an empty list.
        """
        self.db = []

    def get_all_instruments(self):
        """
        Returns all instruments from the database.

        Returns:
        list: List of instruments.
        """
        return self.db

    def add_instrument(self, symbol):
        """
        Appends the provided symbol to the database.

        Parameters:
        symbol (str): The symbol to be added.
        """
        self.db.append(symbol)

    def update_instrument(self, index, symbol):
        """
        Updates the symbol name at the provided index with the newly provided symbol.

        Parameters:
        index (int): The index of the instrument to be updated.
        symbol (str): The new symbol.
        """
        if index < len(self.db):
            self.db[index] = symbol
        else:
            raise HTTPException(status_code=400, detail="No symbol found")

    def remove_instrument(self, index):
        """
        Removes the symbol present at the provided index.

        Parameters:
        index (int): The index of the instrument to be removed.
        """
        if index < len(self.db):
            del self.db[index]
        else:
            raise HTTPException(status_code=400, detail="No symbol found")

# Initialize FastAPI app
app = FastAPI()

# Initialize instrument database
db = InstrumentDatabase()

# Endpoint to return all instruments
@app.get("/instruments")
async def get_instruments():
    return db.get_all_instruments()

# Endpoint to add a symbol
@app.post("/add")
async def add_instrument(symbol: str):
    db.add_instrument(symbol)
    return {"message": f"Symbol {symbol} added successfully"}

# Endpoint to update a symbol
@app.patch("/update")
async def update_instrument(index: int, symbol: str):
    db.update_instrument(index, symbol)
    return {"message": f"Symbol at index {index} updated successfully"}

# Endpoint to remove a symbol
@app.delete("/remove")
async def remove_instrument(index: int):
    db.remove_instrument(index)
    return {"message": f"Symbol at index {index} removed successfully"}
