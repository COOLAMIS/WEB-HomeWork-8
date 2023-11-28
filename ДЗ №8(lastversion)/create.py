from models import TextPost, Authors

if __name__=='__main__':
    Albert_Einstein = Authors(fullname="Albert Einstein", born_date="March 14, 1879", born_location="in Ulm, Germany",
                           description="In 1879, Albert Einstein was born in Ulm, Germany.").save()

    post1 = TextPost(quote="“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”", author=Albert_Einstein)
    post1.tags = ["change", "deep-thoughts", "thinking", "world"]
    post1.save()

    post2 = TextPost(quote='“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”', author=Albert_Einstein)
    post2.tags = ["inspirational", "life", "live", "miracle", "miracles"]
    post2.save()

    post2 = TextPost(quote='“Try not to become a man of success. Rather become a man of value.”', author=Albert_Einstein)
    post2.tags = ["adulthood", "success", "value"]
    post2.save()

    Steve_Martin = Authors(fullname="Steve Martin", born_date="August 14, 1945", born_location="in Waco, Texas, The United States",
                 description="Stephen Glenn \"Steve\" Martin is an American actor, comedian, writer, playwright, producer, musician, and composer.").save()
    
    post3 = TextPost(quote='“A day without sunshine is like, you know, night.”', author=Steve_Martin)
    post3.tags = ["humor", "obvious", "simile"]
    post3.save()