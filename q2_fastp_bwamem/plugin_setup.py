from qiime2.plugin import Plugin
import q2_fastp_bwamem

plugin = Plugin(
    name='fastp-bwamem',
    version=q2_fastp_bwamem.__version__,
    website='https://github.com/CatFish47/q2-fastp-bwamem',
    user_support_text='https://github.com/CatFish47/q2-fastp-bwamem',
    package='q2_fastp_bwamem'
)