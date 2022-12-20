import asyncio 
from pyppeteer import launch 


async def search_for_prape_processes():
    browser =  await launch({"headless": True})

    page = await browser.newPage()
    #await page.setViewport({"width": 1600, "height": 900})

    await page.goto("https://sipac.ufpb.br/public/jsp/processos/consulta_processo.jsf")
    
    interested_field = await page.querySelector("#processoForm > table > tbody > tr:nth-child(2) > td:nth-child(1) > input")
    await interested_field.click()
    await page.waitFor(1000)

    prape_field = await page.querySelector("#processoForm > table > tbody > tr:nth-child(2) > td:nth-child(2) > input")
    await prape_field.type("prape")
    await page.waitFor(1000)

    submit_button = await page.querySelector("#relatorio > td > input[type=submit]")
    await submit_button.click()
    await page.waitFor(3000)
 



print("Starting...")
asyncio.get_event_loop().run_until_complete(
   search_for_prape_processes()
)
print("Finished")