# IT6 PIN Brute Force Challenge

## Description
This project is a Python script that brute-forces a 3-digit PIN (000-999) by sending crafted HTTP POST requests to a local server using raw sockets (without using libraries like `requests`).

The goal was to automate guessing the PIN required by a vulnerable web server challenge.

---

## Solution Process

### Step 1: Finding the Address and Port
- I started the provided server executable (`ctf1_for_x64.exe`).
- Using the command `netstat -aon | findstr LISTENING`, I listed all open ports on my machine.
- I matched the Process ID (PID) of the server to the port and found that it was listening on **127.0.0.1:8888**.
- I confirmed by visiting `http://127.0.0.1:8888` in my browser.

### Step 2: Understanding How to Send the Guess
- I accessed the server through the browser and observed that it required entering a **3-digit PIN**.
- By manually submitting a form and inspecting the network traffic (using the browser DevTools / Postman), I noticed the server expects a POST request containing a `magicNumber` field.
- Therefore, to guess programmatically, I needed to send an HTTP POST request with the field `magicNumber={PIN}`.

### Step 3: Developing the Python Script
- I wrote a Python script using only the `socket` library.
- For each PIN from 000 to 999:
  - Format it as a 3-digit string (e.g., `001`, `042`, etc.).
  - Craft and send a raw HTTP POST request with the current PIN.
  - Analyze the server's HTTP response:
    - If it contains `"Incorrect number"`, continue to the next PIN.
    - Otherwise, the correct PIN has been found.
- I added a `time.sleep(1)` between requests to avoid sending too fast and overwhelming the server.

### Step 4: Testing and Successfully Finding the Correct PIN
- I ran the script and observed that it successfully detected the correct PIN after trying the possible values.

---

## Challenges Encountered
- **Rate limiting by server:**  
  Sending too many requests too quickly made the server slow down or not respond correctly.  
  **Solution:** I added a 1-second delay between each request.
  
- **Raw HTTP formatting:**  
  Since I used sockets directly (no high-level HTTP libraries), I had to manually craft the request format correctly (`\r\n` line breaks, correct headers, Content-Length).

---

## Lessons Learned
- How to use **low-level sockets** to interact with web servers manually.
- How to **craft HTTP requests** manually.
- Understanding how **simple brute-force attacks** can break insecure systems.
- How important **rate-limiting, CAPTCHA, and stronger passwords** are in securing a website.

---

## Improving the Server Security
To defend against this type of attack, I would:
- Implement CAPTCHA after a few failed attempts.
- Rate-limit login attempts.
- Increase PIN complexity (more digits, alphanumeric).
- Block IP addresses after multiple failed attempts.
- Introduce account lockout mechanisms.

---

## References

- [Unblu article on guessing PIN codes](https://www.unblu.com/en/docs/5/knowledge-base/security-guessing-the-pin-code.html) — Helped me understand brute-force logic and server-side protections.
- [A video tutorial in youtube on how to simulate a brute-force attack ethically using Python] (https://www.youtube.com/watch?v=HHOzhtrJJg0) - Help me to learn how to simulate and secure my web by brute-force attack.
