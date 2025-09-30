import cognee
import asyncio

class cogni:
    def __init__(self):
        pass
    async def delete_all(self):
        await cognee.prune.prune_data()
        await cognee.prune.prune_system(metadata=True)
        print("Deleted all data.")

    async def add_content(self, document_link):
        await cognee.add(document_link)
        print(f"Added content from {document_link}")
        # Process with LLMs to build the knowledge graph
        await cognee.cognify()
    
    async def search(self, query_text):
        # Search the knowledge graph
        results = await cognee.search(
            query_text=query_text
        )
        return results

if __name__ == '__main__':
    cog = cogni()
    asyncio.run(cog.delete_all())
    asyncio.run(cog.add_content("ABL_Guide_2.pdf"))
    results = asyncio.run(cog.search("What can I do with myABL?"))
    for result in results:
        print(result)
