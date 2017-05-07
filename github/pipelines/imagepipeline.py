import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

class MyImagesPipeline(ImagesPipeline):

    # def file_path(self, request, response=None, info=None):
    #     """ Name download version """
    #
    #     image_guid = request.url.split('/')[-1]
    #     return 'full/{}'.format(image_guid)
    #
    #
    # def thumb_path(self, request, thumb_id, response=None, info=None):
    #     """ Name thumbnail version """
    #
    #     image_guid = thumb_id + response.url.split('/')[-1]
    #     return 'thumbs/{}/{}.jpg'.format(thumb_id, image_guid)


    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)


    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item