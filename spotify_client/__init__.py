from typing import Any

from spotify_client.client import SpotifyClient
from spotify_client.endpoints.albums import AlbumsEntity


class SpotifyPyClient(SpotifyClient):
    """
    Main class to communicate with the Spotify API
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the class with your api_key and user_id and attach all of the endpoints."""
        super().__init__(*args, **kwargs)

        #         # API Root
        #         self.root = self.api_root = Root(self)
        #         # Authorized Apps
        #         self.authorized_apps = AuthorizedApps(self)
        #         # Automations - Paid feature
        self.albums = AlbumsEntity(self)


#         self.automations.actions = AutomationActions(self)
#         self.automations.emails = AutomationEmails(self)
#         self.automations.emails.actions = AutomationEmailActions(self)
#         self.automations.emails.queues = AutomationEmailQueues(self)
#         self.automations.removed_subscribers = AutomationRemovedSubscribers(self)
#         # Batch Operations
#         self.batches = self.batch_operations = BatchOperations(self)
#         # Batch Webhooks
#         self.batch_webhooks = BatchWebhooks(self)
#         # Campaign Folders
#         self.campaign_folders = CampaignFolders(self)
#         # Campaigns
#         self.campaigns = Campaigns(self)
#         self.campaigns.actions = CampaignActions(self)
#         self.campaigns.content = CampaignContent(self)
#         self.campaigns.feedback = CampaignFeedback(self)
#         self.campaigns.send_checklist = CampaignSendChecklist(self)
#         # Conversations - Paid feature
#         self.conversations = Conversations(self)
#         self.conversations.messages = ConversationMessages(self)
#         # Customer Journey
#         self.journeys = self.customer_journeys = CustomerJourney(self)
#         # E-commerce Stores
#         self.stores = self.ecommerce = Stores(self)
#         self.stores.carts = StoreCarts(self)
#         self.stores.carts.lines = StoreCartLines(self)
#         self.stores.customers = StoreCustomers(self)
#         self.stores.orders = StoreOrders(self)
#         self.stores.orders.lines = StoreOrderLines(self)
#         self.stores.products = StoreProducts(self)
#         self.stores.products.images = StoreProductImages(self)
#         self.stores.products.variants = StoreProductVariants(self)
#         self.stores.promo_rules = StorePromoRules(self)
#         self.stores.promo_codes = StorePromoCodes(self)
#         # File Manager Files
#         self.files = FileManagerFiles(self)
#         # File Manager Folders
#         self.folders = FileManagerFolders(self)
#         # Landinge Pages
#         self.landing_pages = LandingPages(self)
#         self.landing_pages.actions = LandingPageAction(self)
#         self.landing_pages.content = LandingPageContent(self)
#         # Lists
#         self.lists = Lists(self)
#         self.lists.abuse_reports = ListAbuseReports(self)
#         self.lists.activity = ListActivity(self)
#         self.lists.clients = ListClients(self)
#         self.lists.growth_history = ListGrowthHistory(self)
#         self.lists.interest_categories = ListInterestCategories(self)
#         self.lists.interest_categories.interests = ListInterestCategoryInterest(self)
#         self.lists.members = ListMembers(self)
#         self.lists.members.activity = ListMemberActivity(self)
#         self.lists.members.events = ListMemberEvents(self)
#         self.lists.members.goals = ListMemberGoals(self)
#         self.lists.members.notes = ListMemberNotes(self)
#         self.lists.members.tags = ListMemberTags(self)
#         self.lists.merge_fields = ListMergeFields(self)
#         self.lists.segments = ListSegments(self)
#         self.lists.segments.members = ListSegmentMembers(self)
#         self.lists.signup_forms = ListSignupForms(self)
#         self.lists.webhooks = ListWebhooks(self)
#         # Ping
#         self.ping = Ping(self)
#         # Reports
#         self.reports = Reports(self)
#         self.reports.abuse_reports = ReportCampaignAbuseReports(self)
#         self.reports.advice = ReportCampaignAdvice(self)
#         self.reports.click_details = ReportClickDetailReports(self)
#         self.reports.click_details.members = ReportClickDetailMembers(self)
#         self.reports.domain_performance = ReportDomainPerformance(self)
#         self.reports.eepurl = ReportEepURL(self)
#         self.reports.email_activity = ReportEmailActivity(self)
#         self.reports.locations = ReportLocations(self)
#         self.reports.sent_to = ReportSentTo(self)
#         self.reports.subreports = ReportSubReports(self)
#         self.reports.unsubscribes = ReportUnsubscribes(self)
#         self.reports.open_details = ReportOpenDetails(self)
#         self.reports.google_analytics = ReportGoogleAnalytics(self)
#         # Search Campaigns
#         self.search_campaigns = SearchCampaigns(self)
#         # Search Members
#         self.search_members = SearchMembers(self)
#         # Template Folders
#         self.template_folders = TemplateFolders(self)
#         # Templates
#         self.templates = Templates(self)
#         self.templates.default_content = TemplateDefaultContent(self)
