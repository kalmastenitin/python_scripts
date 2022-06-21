import math

def findpages(pages=120, users=1):
    if users <= 1:
        return [f"1-{pages}"]
    dist = math.floor(pages/users)
    if dist*users != pages:
        print("some pages are remaining")
    page_sorting = []
    display_sorting = []
    for user in range(1,users):
        if not(any(page_sorting)):
            page_sorting.append(f"1-{dist}")
            display_sorting.append(dist)
        page_sorting.append(f"{dist*len(page_sorting)+1}-{dist*(len(page_sorting)+1) if len(page_sorting)+1 != users else pages}")
        display_sorting.append(dist*(len(display_sorting)+1) if len(display_sorting)+1 != users else pages) 
    return page_sorting,display_sorting

if __name__=="__main__":
    _sort1, _sort2 = findpages(pages=1027,users=4)
    print("How to send: {}".format(_sort1))
    print("How to display: {}".format(_sort2))
