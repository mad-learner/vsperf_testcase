from django.db import models

#Create your models here.

TAKE_CHOICES = (
            ('phy2phy_tput', 'phy2phy_tput'),
            ('phy2phy_forwarding', 'phy2phy_forwarding'),
            ('phy2phy_learning', 'phy2phy_learning'),
            ('phy2phy_caching', 'phy2phy_caching'),
            ('back2back', 'back2back'),
            ('phy2phy_tput_mod_vlan', 'phy2phy_tput_mod_vlan'),
            ('phy2phy_tput_mod_vlan_cont', 'phy2phy_tput_mod_vlan_cont'),
            ('phy2phy_cont', 'phy2phy_cont'),
            ('phy2phy_burst', 'phy2phy_burst'),
            ('pvp_cont', 'pvp_cont'),
            ('pvvp_cont', 'pvvp_cont'),
            ('pvpv_cont', 'pvpv_cont'),
            ('phy2phy_scalability', 'phy2phy_scalability'),
            ('phy2phy_scalability_cont', 'phy2phy_scalability_cont'),
            ('pvp_tput', 'pvp_tput'),
            ('pvp_back2back', 'pvp_back2back'),
            ('pvvp_tput', 'pvvp_tput'),
            ('pvvp_back2back', 'pvvp_back2back'),
            ('phy2phy_cpu_load', 'phy2phy_cpu_load'),
            ('phy2phy_mem_load', 'phy2phy_mem_load'),
            ('phy2phy_tput_vpp', 'phy2phy_tput_vpp'),
            ('phy2phy_cont_vpp', 'phy2phy_cont_vpp'),
            ('phy2phy_back2back_vpp', 'phy2phy_back2back_vpp'),
            ('pvp_tput_vpp', 'pvp_tput_vpp'),
            ('pvp_cont_vpp', 'pvp_cont_vpp'),
            ('pvp_back2back_vpp', 'pvp_back2back_vpp'),
            ('pvvp_tput_vpp', 'pvvp_tput_vpp'),
            ('pvvp_cont_vpp', 'pvvp_cont_vpp'),
            ('pvvp_back2back_vpp', 'pvvp_back2back_vpp'),
)


class EntryForm(models.Model):
    testcase = models.CharField(max_length=200, choices=TAKE_CHOICES, default='')
    date_created = models.DateField(auto_now_add=True)

   
