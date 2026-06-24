import asyncio
import aiohttp
import random
import string
import time


URL = "https://localhost/iasfinal/vulnerable.php"

REQUESTS_PER_SECOND = 2
TEST_DURATION = 60

stop_sending = False

#d
def generate_user():
    rid = ''.join(
        random.choices(
            string.ascii_lowercase + string.digits,
            k=6
        )
    )

    return {
        "operation": "create",
        "name": f"user_{rid}",
        "email": f"{rid}@test.com",
        "department": "IT"
    }


async def send_request(session):

    data = generate_user()

    try:
        async with session.post(
            URL,
            json=data,
            ssl=False
        ) as response:

            await response.text()

            return response.status

    except Exception as e:
        return str(e)



async def worker(session, count):

    tasks = []

    for _ in range(count):
        tasks.append(
            send_request(session)
        )

    return await asyncio.gather(*tasks)



# Listen for "n" key
async def keyboard_listener():

    global stop_sending

    while True:

        key = await asyncio.to_thread(input)

        if key.lower() == "n":

            stop_sending = True

            print("\nStopping requests...")

            break



async def main():

    global stop_sending


    print("Press ENTER then type n to stop sending requests")


    connector = aiohttp.TCPConnector(
        limit=1000
    )


    async with aiohttp.ClientSession(
        connector=connector
    ) as session:


        # start keyboard watcher
        asyncio.create_task(
            keyboard_listener()
        )


        start = time.time()

        total = 0


        while (
            time.time() - start < TEST_DURATION
            and not stop_sending
        ):


            second_start = time.time()


            results = await worker(
                session,
                REQUESTS_PER_SECOND
            )


            total += len(results)


            success = results.count(200)


            print(
                f"Sent: {len(results)} | "
                f"Success: {success} | "
                f"Total: {total}"
            )



            elapsed = time.time() - second_start


            if elapsed < 1:

                await asyncio.sleep(
                    1 - elapsed
                )



    print("\nFinished")
    print("Total requests:", total)



asyncio.run(main())