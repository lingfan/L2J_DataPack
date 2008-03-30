# Script for Pagan Temple Teleporters
# Needed for Quests 636 and 637
# v1.1 Done by BiTi

import sys
from net.sf.l2j.gameserver.datatables import DoorTable
from net.sf.l2j.gameserver.model.actor.instance import L2PcInstance
from net.sf.l2j.gameserver.model.quest import State
from net.sf.l2j.gameserver.model.quest import QuestState
from net.sf.l2j.gameserver.model.quest.jython import QuestJython as JQuest
qn = "1630_PaganTeleporters"
NPCS=[32034,32035,32036,32037,32039,32040]

# Main Quest Code
class Quest (JQuest):

  def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

  def onEvent (self,event,st) :
    if event == "Close_Door1" :
       DoorTable.getInstance().getDoor(19160001).closeMe()
    elif event == "Close_Door2" :
       DoorTable.getInstance().getDoor(19160010).openMe()
       DoorTable.getInstance().getDoor(19160010).openMe()
    return

  def onTalk (self,npc,player):
    st = player.getQuestState(qn)
    npcId = npc.getNpcId()
    htmltext = ""
    if npcId == 32034 :
          if not st.getQuestItemsCount()in [8064,8065,8067]:
             return "<html><body>The Temple Gatekeeper:<br>You have nothing that would cover the holes.<br>(You must have a Visitor's Mark, a Faded Visitor's Mark, or a Pagan's Mark in order to open this door.)</body></html>"
          if st.getQuestItemsCount(8064) :
             st.takeItems(8064,1) # TODO: this part must happen when u walk through doors >.<
             st.giveItems(8065,1)
          htmltext = "FadedMark.htm"
          DoorTable.getInstance().getDoor(19160001).openMe()
          self.startQuestTimer("Close_Door1",10000,none,none)
    elif npcId == 32035:
          DoorTable.getInstance().getDoor(19160001).openMe()
          self.startQuestTimer("Close_Door1",10000,none,none)
          htmltext = "FadedMark.htm"
    elif npcId == 32036:
       if not st.getQuestItemsCount(8067) :
          htmltext = "<html><body>The Temple Gatekeeper:<br>Show your Mark or be gone from my sight!<br>Only those who possess the Pagan's Mark may pass through this gate!</body></html>"
       else:
          htmltext = "<html><body>The Temple Gatekeeper:<br>On seeing the Pagan's Mark, the statue's probing eyes go blank.<br>With the quiet whir of an engine, the gate swings open...</body></html>"
          self.startQuestTimer("Close_Door2",10000,none,none)
          DoorTable.getInstance().getDoor(19160010).openMe()
          DoorTable.getInstance().getDoor(19160010).openMe()
    elif npcId == 32037:
          DoorTable.getInstance().getDoor(19160010).openMe()
          DoorTable.getInstance().getDoor(19160010).openMe()
          self.startQuestTimer("Close_Door2",10000,none,none)
          htmltext = "FadedMark.htm"
    else :
       if npcId == 32039 :
          player.teleToLocation(-12766,-35840,-10856)
       elif npcId == 32040 :
          player.teleToLocation(36640,-51218,718)
    st.exitQuest(1)
    return htmltext

# Quest class and state definition
QUEST       = Quest(1630, qn, "Teleports")

# Quest NPC starter initialization
for npc in NPCS :
    QUEST.addStartNpc(npc)
    QUEST.addTalkId(npc)
