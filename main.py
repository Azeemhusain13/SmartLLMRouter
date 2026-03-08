from dotenv import load_dotenv
load_dotenv()

from router import SmartLLMRouter


router = SmartLLMRouter()

response = router.ask("Explain Artificial Intelligence simply.")

print("\nAnswer:\n", response)