from scrapy.spiders import Spider
from scrapy.http.request import Request
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from rumahsakit.items import RumahsakitItem
import urlparse

class DepkesSpider(Spider):
    name = "depkes"
    allowed_domains = ["sirs.buk.depkes.go.id"]

    def start_requests(self):
      	for x in range(1, 255):
    		yield self.make_requests_from_url("http://sirs.buk.depkes.go.id/rsonline/Last_Update_report.php?goto=%d" %x)

    def parse(self, response):
    	itemselector = Selector(response).xpath('//table[@class="report"]/tbody/tr')
    	for sel in itemselector:
    		item = RumahsakitItem()
    		item['tgl_update'] = ''.join(map(unicode.strip, sel.xpath('td[1]/p/text()').extract()))
    		item['kode'] = ''.join(map(unicode.strip, sel.xpath('td[2]/p/text()').extract()))
    		item['tgl_registrasi'] = ''.join(map(unicode.strip, sel.xpath('td[3]/p/text()').extract()))
    		item['nama'] = ''.join(map(unicode.strip, sel.xpath('td[4]/p/text()').extract()))
    		item['jenis'] = ''.join(map(unicode.strip, sel.xpath('td[5]/p/text()').extract()))
    		item['kelas'] = ''.join(map(unicode.strip, sel.xpath('td[6]/p/text()').extract()))
    		item['direktur'] = ''.join(map(unicode.strip, sel.xpath('td[7]/p/text()').extract()))
    		item['alamat'] = ''.join(map(unicode.strip, sel.xpath('td[8]/p/text()').extract()))
    		item['penyelenggara'] = ''.join(map(unicode.strip, sel.xpath('td[9]/p/text()').extract()))
    		item['kab_kota'] = ''.join(map(unicode.strip, sel.xpath('td[10]/p/text()').extract()))
    		item['kode_pos'] = ''.join(map(unicode.strip, sel.xpath('td[11]/p/text()').extract()))
    		item['tlp'] = ''.join(map(unicode.strip, sel.xpath('td[12]/p/text()').extract()))
    		item['fax'] = ''.join(map(unicode.strip, sel.xpath('td[13]/p/text()').extract()))
    		item['email'] = ''.join(map(unicode.strip, sel.xpath('td[14]/p/text()').extract()))
    		item['tlp_humas'] = ''.join(map(unicode.strip, sel.xpath('td[15]/p/text()').extract()))
    		item['website'] = ''.join(map(unicode.strip, sel.xpath('td[16]/p/text()').extract()))
    		item['luas_tanah'] = ''.join(map(unicode.strip, sel.xpath('td[17]/p/text()').extract()))
    		item['luas_bangunan'] = ''.join(map(unicode.strip, sel.xpath('td[18]/p/text()').extract()))
    		item['ijin_no'] = ''.join(map(unicode.strip, sel.xpath('td[19]/p/text()').extract()))
    		item['ijin_tgl'] = ''.join(map(unicode.strip, sel.xpath('td[20]/p/text()').extract()))
    		item['ijin_pemberi'] = ''.join(map(unicode.strip, sel.xpath('td[21]/p/text()').extract()))
    		item['ijin_sifat'] = ''.join(map(unicode.strip, sel.xpath('td[22]/p/text()').extract()))
    		item['ijin_masa_berlaku'] = ''.join(map(unicode.strip, sel.xpath('td[23]/p/text()').extract()))
    		item['ijin_status_penyelenggara'] = ''.join(map(unicode.strip, sel.xpath('td[24]/text()').extract()))
    		item['khusus_swasta'] = ''.join(map(unicode.strip, sel.xpath('td[25]/text()').extract()))
    		item['akreditas_pentahapan'] = ''.join(map(unicode.strip, sel.xpath('td[26]/p/text()').extract()))
    		strAkreditasPentahapan = str(item['akreditas_pentahapan'])
    		if strAkreditasPentahapan:
    			item['akreditas_pentahapan'] = strAkreditasPentahapan.replace('I     ( ', 'I (')
    		item['akreditas_status'] = ''.join(map(unicode.strip, sel.xpath('td[27]/p/text()').extract()))
    		item['akreditas_tgl'] = ''.join(map(unicode.strip, sel.xpath('td[28]/text()').extract()))
    		item['bangsal_vvip'] = ''.join(map(unicode.strip, sel.xpath('td[29]/p/text()').extract()))
    		item['bangsal_vip'] = ''.join(map(unicode.strip, sel.xpath('td[30]/p/text()').extract()))
    		item['bangsal_i'] = ''.join(map(unicode.strip, sel.xpath('td[31]/p/text()').extract()))
    		item['bangsal_ii'] = ''.join(map(unicode.strip, sel.xpath('td[32]/p/text()').extract()))
    		item['bangsal_iii'] = ''.join(map(unicode.strip, sel.xpath('td[33]/p/text()').extract()))
    		item['dokter_sp_a'] = ''.join(map(unicode.strip, sel.xpath('td[34]/p/text()').extract()))
    		item['dokter_sp_og'] = ''.join(map(unicode.strip, sel.xpath('td[35]/p/text()').extract()))
    		item['dokter_sp_pd'] = ''.join(map(unicode.strip, sel.xpath('td[36]/p/text()').extract()))
    		item['dokter_sp_b'] = ''.join(map(unicode.strip, sel.xpath('td[37]/p/text()').extract()))
    		item['dokter_sp_rad'] = ''.join(map(unicode.strip, sel.xpath('td[38]/p/text()').extract()))
    		item['dokter_sp_rm'] = ''.join(map(unicode.strip, sel.xpath('td[39]/text()').extract()))
    		item['dokter_sp_an'] = ''.join(map(unicode.strip, sel.xpath('td[40]/p/text()').extract()))
    		item['dokter_sp_jp'] = ''.join(map(unicode.strip, sel.xpath('td[41]/p/text()').extract()))
    		item['dokter_sp_m'] = ''.join(map(unicode.strip, sel.xpath('td[42]/p/text()').extract()))
    		item['dokter_sp_tht'] = ''.join(map(unicode.strip, sel.xpath('td[43]/p/text()').extract()))
    		item['dokter_sp_kj'] = ''.join(map(unicode.strip, sel.xpath('td[44]/p/text()').extract()))
    		item['dokter_umum'] = ''.join(map(unicode.strip, sel.xpath('td[45]/p/text()').extract()))
    		item['dokter_gigi'] = ''.join(map(unicode.strip, sel.xpath('td[46]/p/text()').extract()))
    		item['dokter_sp_gigi'] = ''.join(map(unicode.strip, sel.xpath('td[47]/p/text()').extract()))
    		item['perawat'] = ''.join(map(unicode.strip, sel.xpath('td[48]/p/text()').extract()))
    		item['bidan'] = ''.join(map(unicode.strip, sel.xpath('td[49]/p/text()').extract()))
    		item['farmasi'] = ''.join(map(unicode.strip, sel.xpath('td[50]/p/text()').extract()))
    		item['tenaga_kes_lainnya'] = ''.join(map(unicode.strip, sel.xpath('td[51]/p/text()').extract()))
    		item['tenaga_non_kes'] = ''.join(map(unicode.strip, sel.xpath('td[52]/p/text()').extract()))
    		yield item
	        


