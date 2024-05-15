import dpkt
from selenium import webdriver


def press_button(driver, direction):
    buttons = driver.find_elements("name", "direction")
    if direction == "up":
        buttons[0].click()
    elif direction == "left":
        buttons[1].click()
    elif direction == "right":
        buttons[2].click()
    elif direction == "down":
        buttons[3].click()
    elif direction == "start":
        buttons[0].click()


def main():
    directions = []
    with open("capture.pcap", "rb") as pcap_file:
        pcap = dpkt.pcap.Reader(pcap_file)
        for ts, buf in pcap:
            decoded_buf = buf.decode('utf-8', errors='ignore')
            if "Last Move: FAILED because the maze was busy. Try the move again!" in decoded_buf:
                print("Detected Failed Direction in PCAP")
                directions.pop()
            index = decoded_buf.find("/maze?direction=")
            if index != -1:
                start_index = index + len("/maze?direction=")
                end_index = decoded_buf.find(" ", start_index)
                direction = decoded_buf[start_index:end_index]
                directions.append(direction)

    driver = webdriver.Firefox()
    driver.get("http://blindmazerevenge.challs.open.ecsc2024.it/")

    for direction in directions:
        failed_message = "Last Move: FAILED because the maze was busy. Try the move again!"
        while True:
            press_button(driver, direction)
            try:
                driver.find_element("xpath", f"//*[contains(text(), '{failed_message}')]")
                found_fail = True
            except Exception:
                found_fail = False
            if not found_fail:
                break


if __name__ == "__main__":
    main()