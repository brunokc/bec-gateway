from pyproxy import HttpRequest, HttpResponse
from typing import List

from . import BaseHandler, DataSetType, ProcessingResult

"""
<system version="1.7">
    <config>
        <mode>auto</mode>
        <cfgem>F</cfgem>
        <cfgauto>on</cfgauto>
        <cfgtype>heatcool</cfgtype>
        <cfgdead>2</cfgdead>
        <cfgcph>4</cfgcph>
        <cfgfan>on</cfgfan>
        <cfgpgm>on</cfgpgm>
        <cfgchgovr>30</cfgchgovr>
        <cfgsimultheatcool />
        <cfgrecovery>on</cfgrecovery>
        <cfgzoning>on</cfgzoning>
        <cfghumid>off</cfghumid>
        <cfgvent>off</cfgvent>
        <cfguv>off</cfguv>
        <filtertype>air filter</filtertype>
        <filterinterval>3</filterinterval>
        <ventinterval>90</ventinterval>
        <uvinterval>12</uvinterval>
        <huminterval>12</huminterval>
        <humidityfan>off</humidityfan>
        <statpressmon>off</statpressmon>
        <odtmpoff>0</odtmpoff>
        <humoff>0</humoff>
        <ducthour>13</ducthour>
        <heatsource>system</heatsource>
        <erate>0.13</erate>
        <grate>1.60</grate>
        <fueltype>gas</fueltype>
        <gasunit>therm</gasunit>
        <blight>80</blight>
        <screensaver>off</screensaver>
        <sound>on</sound>
        <filtrrmd>on</filtrrmd>
        <humrmd>on</humrmd>
        <ventrmd>on</ventrmd>
        <uvrmd>on</uvrmd>
        <windowprotect>
            <enabled>on</enabled>
            <rhtg>9</rhtg>
            <ventprotect>off</ventprotect>
        </windowprotect>
        <humidityHome>
            <humid>manual</humid>
            <rhtg>4</rhtg>
            <rclg>4</rclg>
            <rclgovercool>on</rclgovercool>
            <humidifier>on</humidifier>
            <venthtg>auto</venthtg>
            <ventspdhtg>high</ventspdhtg>
            <ventclg>auto</ventclg>
            <ventspdclg>high</ventspdclg>
        </humidityHome>
        <humidityAway>
            <humid>off</humid>
            <rhtg>1</rhtg>
            <rclg>15</rclg>
            <rclgovercool>off</rclgovercool>
            <humidifier>off</humidifier>
            <venthtg>off</venthtg>
            <ventspdhtg>high</ventspdhtg>
            <ventclg>off</ventclg>
            <ventspdclg>high</ventspdclg>
        </humidityAway>
        <humidityVacation>
            <rhtg>1</rhtg>
            <rclg>15</rclg>
            <rclgovercool>off</rclgovercool>
            <humidifier>off</humidifier>
            <venthtg>off</venthtg>
            <ventspdhtg>high</ventspdhtg>
            <ventclg>off</ventclg>
            <ventspdclg>high</ventspdclg>
        </humidityVacation>
        <vacat>off</vacat>
        <vacstart />
        <vacend />
        <vacmint>60.0</vacmint>
        <vacmaxt>80.0</vacmaxt>
        <vacfan>off</vacfan>
        <torqueControl>off</torqueControl>
        <staticPressure>1.02</staticPressure>
        <calcMinCFM>300</calcMinCFM>
        <blowerSpeed>1299</blowerSpeed>
        <systemCFM>1400</systemCFM>
        <blowerActualCFM />
        <blowerCoolingCFM />
        <blowerHeatingCFM />
        <blowerPower />
        <utilityEvent>
            <enabled>false</enabled>
            <priceResp>offset</priceResp>
            <priceLimit>10</priceLimit>
            <priceOffset>4</priceOffset>
            <priceHtAbs>60</priceHtAbs>
            <priceClAbs>82</priceClAbs>
            <demandResp>offset</demandResp>
            <demandOffset>4</demandOffset>
            <demandHtAbs>60</demandHtAbs>
            <demandClAbs>82</demandClAbs>
            <minLimit>50</minLimit>
            <maxLimit>90</maxLimit>
            <restoreDefaults>off</restoreDefaults>
        </utilityEvent>
        <wholeHouse>
            <holdActivity>none</holdActivity>
            <hold>off</hold>
            <otmr />
            <activities>
                <activity id="home">
                    <blight>80</blight>
                </activity>
                <activity id="away">
                    <blight>80</blight>
                </activity>
                <activity id="sleep">
                    <blight>80</blight>
                </activity>
                <activity id="wake">
                    <blight>80</blight>
                </activity>
                <activity id="manual">
                    <blight>80</blight>
                </activity>
            </activities>
        </wholeHouse>
        <weatherPostalCode>98052</weatherPostalCode>
        <zones>
            <zone id="1">
                <name>ZONE 1</name>
                <enabled>on</enabled>
                <holdActivity>manual</holdActivity>
                <hold>on</hold>
                <otmr />
                <setback>on</setback>
                <airflowlimit>high</airflowlimit>
                <cfmlimit>4500</cfmlimit>
                <tempoffset>-4</tempoffset>
                <activities>
                    <activity id="home">
                        <htsp>68.0</htsp>
                        <clsp>74.0</clsp>
                        <fan>off</fan>
                    </activity>
                    <activity id="away">
                        <htsp>62.0</htsp>
                        <clsp>74.0</clsp>
                        <fan>off</fan>
                    </activity>
                    <activity id="sleep">
                        <htsp>66.0</htsp>
                        <clsp>70.0</clsp>
                        <fan>off</fan>
                    </activity>
                    <activity id="wake">
                        <htsp>68.0</htsp>
                        <clsp>74.0</clsp>
                        <fan>off</fan>
                    </activity>
                    <activity id="manual">
                        <htsp>66.0</htsp>
                        <clsp>70.0</clsp>
                        <fan>off</fan>
                    </activity>
                </activities>
                <program>
                    <day id="Sunday">
                        <period id="1">
                            <activity>wake</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>home</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>00:00</time>
                            <enabled>off</enabled>
                        </period>
                        <period id="4">
                            <activity>home</activity><time>00:00</time>
                            <enabled>off</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>21:30</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Monday">
                        <period id="1">
                            <activity>wake</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>home</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>00:00</time>
                            <enabled>off</enabled>
                        </period>
                        <period id="4">
                            <activity>home</activity><time>00:00</time>
                            <enabled>off</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>21:30</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Tuesday">
                        <period id="1">
                            <activity>wake</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>home</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>00:00</time>
                            <enabled>off</enabled>
                        </period>
                        <period id="4">
                            <activity>home</activity><time>00:00</time>
                            <enabled>off</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>21:30</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Wednesday">
                        <period id="1">
                            <activity>wake</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>home</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>00:00</time>
                            <enabled>off</enabled>
                        </period>
                        <period id="4">
                            <activity>home</activity><time>00:00</time>
                            <enabled>off</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>21:30</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Thursday">
                        <period id="1">
                            <activity>wake</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>home</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>00:00</time>
                            <enabled>off</enabled>
                        </period>
                        <period id="4">
                            <activity>home</activity><time>00:00</time>
                            <enabled>off</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>21:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Friday">
                        <period id="1">
                            <activity>wake</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>home</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>00:00</time>
                            <enabled>off</enabled>
                        </period>
                        <period id="4">
                            <activity>home</activity><time>00:00</time>
                            <enabled>off</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>21:30</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Saturday">
                        <period id="1">
                            <activity>wake</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>home</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>00:00</time>
                            <enabled>off</enabled>
                        </period>
                        <period id="4">
                            <activity>home</activity><time>00:00</time>
                            <enabled>off</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>21:30</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                </program>
            </zone>
            <zone id="2">
                <name>Zone 2</name>
                <enabled>off</enabled>
                <holdActivity />
                <hold>off</hold>
                <otmr />
                <setback>on</setback>
                <airflowlimit>high</airflowlimit>
                <cfmlimit>0</cfmlimit>
                <tempoffset>0</tempoffset>
                <activities>
                    <activity id="home">
                        <htsp>68.0</htsp>
                        <clsp>76.0</clsp>
                        <fan>off</fan>
                    </activity>
                    <activity id="away">
                        <htsp>60.0</htsp>
                        <clsp>80.0</clsp>
                        <fan>off</fan>
                    </activity>
                    <activity id="sleep">
                        <htsp>68.0</htsp>
                        <clsp>76.0</clsp>
                        <fan>off</fan>
                    </activity>
                    <activity id="wake">
                        <htsp>68.0</htsp>
                        <clsp>76.0</clsp>
                        <fan>off</fan>
                    </activity>
                    <activity id="manual">
                        <htsp>68.0</htsp>
                        <clsp>76.0</clsp>
                        <fan>off</fan>
                    </activity>
                </activities>
                <program>
                    <day id="Sunday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Monday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Tuesday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Wednesday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Thursday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Friday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Saturday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                </program>
            </zone>
            <zone id="3">
                <name>Zone 3</name>
                <enabled>off</enabled>
                <holdActivity />
                <hold>off</hold>
                <otmr />
                <setback>on</setback>
                <airflowlimit>high</airflowlimit>
                <cfmlimit>0</cfmlimit>
                <tempoffset>0</tempoffset>
                <activities>
                    <activity id="home">
                        <htsp>68.0</htsp>
                        <clsp>76.0</clsp>
                        <fan>off</fan>
                    </activity>
                    <activity id="away">
                        <htsp>60.0</htsp>
                        <clsp>80.0</clsp>
                        <fan>off</fan>
                    </activity>
                    <activity id="sleep">
                        <htsp>68.0</htsp>
                        <clsp>76.0</clsp>
                        <fan>off</fan>
                    </activity>
                    <activity id="wake">
                        <htsp>68.0</htsp>
                        <clsp>76.0</clsp>
                        <fan>off</fan>
                    </activity>
                    <activity id="manual">
                        <htsp>68.0</htsp>
                        <clsp>76.0</clsp>
                        <fan>off</fan>
                    </activity>
                </activities>
                <program>
                    <day id="Sunday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Monday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Tuesday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Wednesday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Thursday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Friday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Saturday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                </program>
            </zone>
            <zone id="4">
                <name>Zone 4</name>
                <enabled>off</enabled>
                <holdActivity />
                <hold>off</hold>
                <otmr />
                <setback>on</setback>
                <airflowlimit>high</airflowlimit>
                <cfmlimit>0</cfmlimit>
                <tempoffset>0</tempoffset>
                <activities>
                    <activity id="home">
                        <htsp>68.0</htsp>
                        <clsp>76.0</clsp>
                        <fan>off</fan>
                    </activity>
                    <activity id="away">
                        <htsp>60.0</htsp>
                        <clsp>80.0</clsp>
                        <fan>off</fan>
                    </activity>
                    <activity id="sleep">
                        <htsp>68.0</htsp>
                        <clsp>76.0</clsp>
                        <fan>off</fan>
                    </activity>
                    <activity id="wake">
                        <htsp>68.0</htsp>
                        <clsp>76.0</clsp>
                        <fan>off</fan>
                    </activity>
                    <activity id="manual">
                        <htsp>68.0</htsp>
                        <clsp>76.0</clsp>
                        <fan>off</fan>
                    </activity>
                </activities>
                <program>
                    <day id="Sunday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Monday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Tuesday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Wednesday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Thursday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Friday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Saturday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                </program>
            </zone>
            <zone id="5">
                <name>Zone 5</name>
                <enabled>off</enabled>
                <holdActivity />
                <hold>off</hold>
                <otmr />
                <setback>on</setback>
                <airflowlimit>high</airflowlimit>
                <cfmlimit>0</cfmlimit>
                <tempoffset>0</tempoffset>
                <activities>
                    <activity id="home">
                        <htsp>68.0</htsp>
                        <clsp>76.0</clsp>
                        <fan>off</fan>
                    </activity>
                    <activity id="away">
                        <htsp>60.0</htsp>
                        <clsp>80.0</clsp>
                        <fan>off</fan>
                    </activity>
                    <activity id="sleep">
                        <htsp>68.0</htsp>
                        <clsp>76.0</clsp>
                        <fan>off</fan>
                    </activity>
                    <activity id="wake">
                        <htsp>68.0</htsp>
                        <clsp>76.0</clsp>
                        <fan>off</fan>
                    </activity>
                    <activity id="manual">
                        <htsp>68.0</htsp>
                        <clsp>76.0</clsp>
                        <fan>off</fan>
                    </activity>
                </activities>
                <program>
                    <day id="Sunday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Monday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Tuesday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Wednesday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Thursday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Friday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Saturday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                </program>
            </zone>
            <zone id="6">
                <name>Zone 6</name>
                <enabled>off</enabled>
                <holdActivity />
                <hold>off</hold>
                <otmr />
                <setback>on</setback>
                <airflowlimit>high</airflowlimit>
                <cfmlimit>0</cfmlimit>
                <tempoffset>0</tempoffset>
                <activities>
                    <activity id="home">
                        <htsp>68.0</htsp>
                        <clsp>76.0</clsp>
                        <fan>off</fan>
                    </activity>
                    <activity id="away">
                        <htsp>60.0</htsp>
                        <clsp>80.0</clsp>
                        <fan>off</fan>
                    </activity>
                    <activity id="sleep">
                        <htsp>68.0</htsp>
                        <clsp>76.0</clsp>
                        <fan>off</fan>
                    </activity>
                    <activity id="wake">
                        <htsp>68.0</htsp>
                        <clsp>76.0</clsp>
                        <fan>off</fan>
                    </activity>
                    <activity id="manual">
                        <htsp>68.0</htsp>
                        <clsp>76.0</clsp>
                        <fan>off</fan>
                    </activity>
                </activities>
                <program>
                    <day id="Sunday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Monday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Tuesday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Wednesday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Thursday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Friday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Saturday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                </program>
            </zone>
            <zone id="7">
                <name>Zone 7</name>
                <enabled>off</enabled>
                <holdActivity />
                <hold>off</hold>
                <otmr />
                <setback>on</setback>
                <airflowlimit>high</airflowlimit>
                <cfmlimit>0</cfmlimit>
                <tempoffset>0</tempoffset>
                <activities>
                    <activity id="home">
                        <htsp>68.0</htsp>
                        <clsp>76.0</clsp>
                        <fan>off</fan>
                    </activity>
                    <activity id="away">
                        <htsp>60.0</htsp>
                        <clsp>80.0</clsp>
                        <fan>off</fan>
                    </activity>
                    <activity id="sleep">
                        <htsp>68.0</htsp>
                        <clsp>76.0</clsp>
                        <fan>off</fan>
                    </activity>
                    <activity id="wake">
                        <htsp>68.0</htsp>
                        <clsp>76.0</clsp>
                        <fan>off</fan>
                    </activity>
                    <activity id="manual">
                        <htsp>68.0</htsp>
                        <clsp>76.0</clsp>
                        <fan>off</fan>
                    </activity>
                </activities>
                <program>
                    <day id="Sunday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Monday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Tuesday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Wednesday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Thursday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Friday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Saturday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                </program>
            </zone>
            <zone id="8">
                <name>Zone 8</name>
                <enabled>off</enabled>
                <holdActivity />
                <hold>off</hold>
                <otmr />
                <setback>on</setback>
                <airflowlimit>high</airflowlimit>
                <cfmlimit>0</cfmlimit>
                <tempoffset>0</tempoffset>
                <activities>
                    <activity id="home">
                        <htsp>68.0</htsp>
                        <clsp>76.0</clsp>
                        <fan>off</fan>
                    </activity>
                    <activity id="away">
                        <htsp>60.0</htsp>
                        <clsp>80.0</clsp>
                        <fan>off</fan>
                    </activity>
                    <activity id="sleep">
                        <htsp>68.0</htsp>
                        <clsp>76.0</clsp>
                        <fan>off</fan>
                    </activity>
                    <activity id="wake">
                        <htsp>68.0</htsp>
                        <clsp>76.0</clsp>
                        <fan>off</fan>
                    </activity>
                    <activity id="manual">
                        <htsp>68.0</htsp>
                        <clsp>76.0</clsp>
                        <fan>off</fan>
                    </activity>
                </activities>
                <program>
                    <day id="Sunday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Monday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Tuesday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Wednesday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Thursday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Friday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                    <day id="Saturday">
                        <period id="1">
                            <activity>home</activity><time>06:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="2">
                            <activity>away</activity><time>08:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="3">
                            <activity>home</activity><time>17:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="4">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                        <period id="5">
                            <activity>sleep</activity><time>22:00</time>
                            <enabled>on</enabled>
                        </period>
                    </day>
                </program>
            </zone>
        </zones>
    </config>
</system>
"""

class SystemHandler(BaseHandler):
    def __init__(self) -> None:
        self.method = "POST"
        self.url_template = r"/systems/([^/]+)$"
        self.type = DataSetType.System
        # self.request_map = request_map
        # self.response_map = response_map

    async def process_request(self, matches: List[str], request: HttpRequest) -> ProcessingResult:
        # dataset = await self.process_form_data(request)
        # keys = { "serial_number": matches[0] }
        # return ProcessingResult(self.type, keys, dataset)
        return ProcessingResult.Empty

    async def process_response(self, matches: List[str], response: HttpResponse) -> ProcessingResult:
        # dataset = await self.process_response_data(response)
        # keys = { "serial_number": matches[0] }
        # return ProcessingResult(DataSetType.PingRates, keys, dataset)
        return ProcessingResult.Empty
