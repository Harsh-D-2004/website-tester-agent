from browser_use import Agent, ChatAnthropic , ChatGoogle
from browser_use import Browser
from dotenv import load_dotenv
import asyncio

load_dotenv()

class WebsiteTester:

    llm : ChatAnthropic
    sys_prompt : str
    url : str

    def __init__(self, llm, sys_prompt, url):
        self.llm = llm
        self.sys_prompt = sys_prompt
        self.url = url

    async def run_agent(self , task, browser):

        agent = Agent(task=task, llm=self.llm , browser=browser , save_conversation_path_encoding="utf-8" , flash_mode=True , 
                      save_conversation_path="./convo2" , extend_system_message= self.sys_prompt , max_actions_per_step=3,
                      available_file_paths=["./results/tester1.txt", "./results/tester2.txt", "./results/tester3.txt"])
        result = await agent.run(max_steps=10)
        return result

    async def product_page_tester(self):

        browser = Browser(headless=True)

        task = open("prompts/page_tester_prompt.txt", "r").read().replace("{url}", self.url)

        ret = await self.run_agent(task , browser)
        return ret

    async def images_tester(self):
        
        browser = Browser(headless=True)

        task = open("prompts/image_tester_prompt.txt", "r").read().replace("{url}", self.url)
        
        ret = await self.run_agent(task , browser)
        return ret

    async def network_config_tester(self):

        browser = Browser(headless=True, record_har_path="./network_trace.har")

        task = task = open("prompts/network_tester_prompt.txt", "r").read().replace("{url}", self.url)

        ret = await self.run_agent(task , browser)
        return ret

async def main():
    # llm = ChatGoogle(model="gemini-2.5-flash")
    llm = ChatAnthropic(model="claude-sonnet-4-0")
    url = input("Enter the URL of the website to test: ")
    sys_prompt = open("prompts/system_prompt.txt", "r").read()

    tester = WebsiteTester(llm, sys_prompt, url)

    while True:
        print("\n===== Agent Menu =====")
        print("1. Product Page Tester")
        print("2. Image Tester")
        print("3. Network Config Tester")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            print("\nRunning Product Page Tester...\n")
            product_page_result = await tester.product_page_tester()
            print("Product Page Result:", product_page_result)

        elif choice == "2":
            print("\nRunning Image Tester...\n")
            images_result = await tester.images_tester()
            print("Images Result:", images_result)

        elif choice == "3":
            print("\nRunning Network Config Tester...\n")
            network_result = await tester.network_config_tester()
            print("Network Result:", network_result)

        elif choice == "4":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    asyncio.run(main())