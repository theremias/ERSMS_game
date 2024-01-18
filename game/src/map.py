from node import Node, Protection_possibility
from climbing_section import Climbing_section, Character
from crag import Crag

def create_map() -> Crag:
    """Returns a Crag."""
    app = Node("APP", 0)
    """chimney route"""
    chi1 = Node("CHI_1", 1, Protection_possibility.BOLT)
    chi2 = Node("CHI_2", 2)
    chi3 = Node("CHI_3", 3)
    chi4 = Node("CHI_4", 4)
    chi5 = Node("CHI_5", 5, Protection_possibility.HOURGLASS)
    chi6 = Node("CHI_6", 6)
    chi7 = Node("CHI_7", 7)
    chi8 = Node("CHI_8", 8, Protection_possibility.HOURGLASS)
    """crack routes"""
    cra2 = Node("CRA_2", 2)
    """left crack route"""
    lcra3 = Node("LCRA_3", 3, Protection_possibility.CRACK)
    lcra4 = Node("LCRA_4", 4, Protection_possibility.HOURGLASS)
    lcra5 = Node("LCRA_5", 5, Protection_possibility.RING)
    lcra6 = Node("LCRA_6", 6, Protection_possibility.CRACK)
    lcra7 = Node("LCRA_7", 7, Protection_possibility.RING)
    """right crack route"""
    rcra3 = Node("RCRA_3", 3, Protection_possibility.HOURGLASS)
    rcra4 = Node("RCRA_4", 4, Protection_possibility.BOLT)
    rcra5 = Node("RCRA_5", 5)
    rcra6 = Node("RCRA_6", 6, Protection_possibility.CRACK)
    rcra7 = Node("RCRA_7", 7)
    """slab routes"""
    slb1 = Node("SLB_1", 1, Protection_possibility.RING)
    """left slab route"""
    lslb2 = Node("LSLB_2", 2)
    lslb3 = Node("LSLB_3", 3, Protection_possibility.HOURGLASS)
    lslb4 = Node("LSLB_4", 4, Protection_possibility.RING)
    lslb5 = Node("LSLB_5", 5)
    lslb6 = Node("LSLB_6", 6, Protection_possibility.RING)
    lslb7 = Node("LSLB_7", 7)
    """right slab route"""
    rslb2 = Node("RSLB_2", 2, Protection_possibility.CRACK)
    rslb3 = Node("RSLB_3", 3, Protection_possibility.RING)
    rslb4 = Node("RSLB_4", 4)
    rslb5 = Node("RSLB_5", 5, Protection_possibility.CRACK)
    rslb6 = Node("RSLB_6", 6)
    rslb7 = Node("RSLB_7", 7)
    slb8 = Node("SLB_8", 8, Protection_possibility.HOURGLASS)
    """overhang routes"""
    ovh1 = Node("OVH_1", 1, Protection_possibility.BOLT)
    ovh2 = Node("OVH_2", 2, Protection_possibility.HOURGLASS)
    ovh3 = Node("OVH_3", 3, Protection_possibility.BOLT)
    ovh4 = Node("OVH_4", 4)
    ovh5 = Node("OVH_5", 5, Protection_possibility.BOLT)
    ovh6 = Node("OVH_6", 6)
    ovh7 = Node("OVH_7", 7, Protection_possibility.BOLT)
    lovh8 = Node("LOVH_8", 8, Protection_possibility.HOURGLASS)
    rovh8 = Node("ROVH_8", 8, Protection_possibility.BOLT)

    tr3 = Node("TR_3", 3)
    tr4 = Node("TR_4", 4, Protection_possibility.BOLT)

    bli6 = Node("BLI_6", 6, Protection_possibility.HOURGLASS)
    bli7 = Node("BLI_7", 7, Protection_possibility.CRACK)

    ab_chi = Node("abseil - chimney", 9, Protection_possibility.RING)
    ab_slb = Node("abseil - slab", 9, Protection_possibility.RING)
    ab_ovh = Node("abseil - overhang", 9, Protection_possibility.RING)

    top_book = Node("TB", 10)

    schi0 = Climbing_section(app, chi1, 0, 0)
    sslb0 = Climbing_section(app, slb1, 0, 0)
    sovh0 = Climbing_section(app, ovh1, 0, 0)

    schi1 = Climbing_section(chi1, chi2, 1, 1)
    scra1 = Climbing_section(chi1, cra2, 1, 2)
    slsl1 = Climbing_section(slb1, lslb2, 0, 1)
    srsl1 = Climbing_section(slb1, rslb2, 0, 2)
    sovh1 = Climbing_section(ovh1, ovh2, 1, 0)

    schi2 = Climbing_section(chi2, chi3, 2, 1)
    slcr2 = Climbing_section(cra2, lcra3, 1, 3)
    srcr2 = Climbing_section(cra2, rcra3, 2, 4)
    slsl2 = Climbing_section(lslb2, lslb3, 0, 1)
    srsl2 = Climbing_section(rslb2, rslb3, 1, 3)
    stra2 = Climbing_section(rslb2, tr3, 0, 3)
    sovh2 = Climbing_section(ovh2, ovh3, 2, 0)

    schi3 = Climbing_section(chi3, chi4, 0, 1)
    slcr3 = Climbing_section(lcra3, lcra4, 2, 4)
    srcr3 = Climbing_section(rcra3, rcra4, 3, 5)
    slsl3 = Climbing_section(lslb3, lslb4, 0, 2)
    srsl3 = Climbing_section(rslb3, rslb4, 1, 4)
    stra3 = Climbing_section(tr3, tr4, 1, 3)
    sovh3 = Climbing_section(ovh3, ovh4, 5, 0)
    sovch = Climbing_section(ovh3, chi4, 4, 4)

    schi4 = Climbing_section(chi4, chi5, 2, 2)
    slcr4 = Climbing_section(lcra4, lcra5, 1, 4)
    slrcr4 = Climbing_section(lcra4, rcra5, 0, 4)
    srlcr4 = Climbing_section(rcra4, lcra5, 1, 3)
    srcr4 = Climbing_section(rcra4, rcra5, 3, 6)
    slsl4 = Climbing_section(lslb4, lslb5, 1, 2)
    slrsl4 = Climbing_section(lslb4, rslb5, 1, 3)
    srsl4 = Climbing_section(rslb4, rslb5, 2, 5)
    stra4 = Climbing_section(tr4, ovh5, 0, 4)
    sovh4 = Climbing_section(ovh4, ovh5, 6, 0)

    schi5 = Climbing_section(chi5, chi6, 1, 2)
    slcr5 = Climbing_section(lcra5, lcra6, 2, 3)
    srcr5 = Climbing_section(rcra5, rcra6, 2, 4)
    sslcr5 = Climbing_section(lslb5, rcra6, 1, 3)
    slsl5 = Climbing_section(lslb5, lslb6, 0, 3)
    srsl5 = Climbing_section(rslb5, rslb6, 0, 4)
    sovh5 = Climbing_section(ovh5, ovh6, 6, 2)
    sbli5 = Climbing_section(ovh5, bli6, 5, 3)

    schi6 = Climbing_section(chi6, chi7, 1, 1)
    slcr6 = Climbing_section(lcra6, lcra7, 3, 3)
    srcr6 = Climbing_section(rcra6, rcra7, 3, 2)
    slsl6 = Climbing_section(lslb6, lslb7, 1, 2)
    srsl6 = Climbing_section(rslb6, rslb7, 1, 5)
    sovh6 = Climbing_section(ovh6, ovh7, 7, 2)
    sbli6 = Climbing_section(bli6, bli7, 5, 5)

    schi7 = Climbing_section(chi7, chi8, 2, 2)
    slcr7 = Climbing_section(lcra7, chi8, 1, 4)
    slsl7 = Climbing_section(lslb7, slb8, 1, 4)
    srsl7 = Climbing_section(rslb7, slb8, 1, 4)
    slov7 = Climbing_section(ovh7, lovh8, 5, 3)
    srov7 = Climbing_section(ovh7, rovh8, 4, 4)

    schi8 = Climbing_section(chi8, ab_chi, 1, 0)
    sslb8 = Climbing_section(slb8, ab_slb, 1, 5)
    slov8 = Climbing_section(lovh8, ab_ovh, 6, 6)
    srov8 = Climbing_section(rovh8, ab_ovh, 4, 6)

    schi9 = Climbing_section(ab_chi, top_book, 0, 1)
    sslb9 = Climbing_section(ab_slb, top_book, 0, 1)
    sovh9 = Climbing_section(ab_ovh, top_book, 1, 0)

    route_list = [schi0, sslb0, sovh0, 
                    schi1, scra1, slsl1, srsl1, sovh1, 
                    schi2, slcr2, srcr2, slsl2, srsl2, stra2, sovh2, 
                    schi3, slcr3, srcr3, slsl3, srsl3, stra3, sovh3, sovch, 
                    schi4, slcr4, slrcr4, srlcr4, srcr4, slsl4, slrsl4, srsl4, stra4, sovh4, 
                    schi5, slcr5, srcr5, sslcr5, slsl5, srsl5, sovh5, sbli5, 
                    schi6, slcr6, srcr6, slsl6, srsl6, sovh6, sbli6, 
                    schi7, slcr7, slsl7, srsl7, slov7, srov7, 
                    schi8, sslb8, slov8, srov8, 
                    schi9, sslb9, sovh9]
    
    crag = Crag(route_list, app, top_book)
    return crag


"""bot1 = Node("BOT1")  
        cra1 = Node("CRA1", Protection_possibility.BOLT)
        cra1.change_height(2)
        cra2 = Node("CRA2", Protection_possibility.HOURGLASS)
        cra2.change_height(5)
        cra3 = Node("CRA3", Protection_possibility.CRACK)
        cra3.change_height(7)
        top1 = Node("TOP1", Protection_possibility.RING)
        top1.change_height(12)
        bli1 = Node("BLI1", Protection_possibility.NOTHING)
        bli1.change_height(6)
        sid1 = Node("SID1", Protection_possibility.CRACK)
        sid1.change_height(6)

        sec1 = Climbing_section(bot1, cra1)
        sec2 = Climbing_section(cra1, cra2, str_diff=2, character=Character.CRIMPS) 
        sec3 = Climbing_section(cra2, cra3, character=Character.CRIMPS)
        sec4 = Climbing_section(cra3, top1)
        sec5 = Climbing_section(cra1, bli1)
        sec6 = Climbing_section(cra2, sid1)
        sec7 = Climbing_section(sid1, cra3, 2, 3)
        route_list = [sec1, sec2, sec3, sec4, sec5, sec6, sec7]"""