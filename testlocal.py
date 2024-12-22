import asyncio
from aiosmtpd.controller import Controller
from aiosmtpd.handlers import Debugging

async def main():
    controller = Controller(Debugging(), hostname='localhost', port=1025)
    controller.start()
    print("SMTP server is running on localhost:1025")
    await asyncio.sleep(3600)  # 1時間動作
    controller.stop()

if __name__ == '__main__':
    asyncio.run(main())