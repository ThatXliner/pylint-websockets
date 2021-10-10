"""Some test"""
import websockets


async def run_client() -> None:
    """Some func"""
    async with websockets.connect("ws://localhost:80") as connection:
        await connection.send("hello")
