all_product = response.css('article.product_pod')
title = response.css('img.thumbnail').attrib['alt']
price = response.css('p.price_color::text').get()
